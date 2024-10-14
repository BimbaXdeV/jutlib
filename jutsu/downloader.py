from bs4 import BeautifulSoup
from tqdm import tqdm
import requests
import os

from .config import *
from .errors import *


class JutSu:
    def __init__(self, url: str):
        self.config: Config = Config(
            download_res=1080,
            name_separator='_',
            register_style='default'
        )

        self.url: str = url
        self.__page: BeautifulSoup | None = None
        self.__episode_name: str | None = None
        self.__video_url: str | None = None

    def set_episode_name(self, name: str = 'Unnamed'):
        if self.__episode_name is None:
            raise WrongSequence('before setting a custom episode title, upload it.')
        self.__episode_name = name

    def name_to_register(self) -> str:
        __stylized_name = self.config.name_separator.join(self.__episode_name.split())

        if self.config.register_style == self.config.register_styles[0]:
            return __stylized_name

        elif self.config.register_style == self.config.register_styles[1]:
            return __stylized_name.upper()

        elif self.config.register_style == self.config.register_styles[2]:
            return __stylized_name.lower()

    @staticmethod
    def get_project_root() -> str:
        return os.path.abspath(os.path.dirname(__file__))

    def get_original_name(self) -> str: return self.__episode_name
    def get_direct_link(self) -> str: return self.__video_url

    def load(self):
        if self.url.split('/')[0] != self.config.website_protocol_trigger:
            raise InvalidServiceProtocol('the link address must contain the https protocol. Open the expanded link in your browser and copy it into the input line.')

        if self.url.split('/')[2] != self.config.service_trigger:
            raise InvalidServiceUrl(f'script correctly working only with \"{self.config.service_trigger}\" service.')

        __page = BeautifulSoup(requests.get(self.url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'}).text, 'lxml')
        __title = __page.find('h1', class_='header_video allanimevideo the_hildi anime_padding_for_title_post')
        if __title is None:
            raise InvalidUrlPage('no episode page found for your request')
        self.__episode_name = ' '.join(__title.find('span', itemprop='name').text.split()[1::])
        self.__video_url = __page.find('div', class_='border_around_video is-no-top-left-border is-no-bottom-right-border no-top-right-border').find('video', class_='video-js vjs-default-skin vjs-16-9').find('source', res=str(self.config.download_res)).get('src')

    def configure(self, download_res: int | None = None, name_separator: str | None = None, register_style: str | None = None):
        if register_style not in self.config.register_styles:
            raise IncorrectRegisterStyle(f'style \"{register_style}\" has not exists.')

        __download_res = self.config.download_res if download_res is None else download_res
        __name_separator = self.config.name_separator if name_separator is None else name_separator
        __register_style = self.config.register_style if register_style is None else register_style

        self.config = Config(__download_res, __name_separator, __register_style)

    def download(self):
        __path = os.path.join(self.get_project_root(), self.name_to_register() + '.mp4')
        __video = requests.get(self.__video_url, stream=True, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'})

        __total_size = int(__video.headers.get('content-length'))
        with open(__path, 'wb') as file, tqdm(
            desc=self.get_original_name(),
            total=__total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
            colour='white'
        ) as progress_bar:
            for chunk in __video.iter_content(chunk_size=8192):
                file.write(chunk)
                progress_bar.update(len(chunk))

        print(f'Video \"{self.__episode_name}\" has been saved to \"{__path}\".')
