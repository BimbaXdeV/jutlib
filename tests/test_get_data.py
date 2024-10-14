from jutsu.downloader import JutSu


if __name__ == '__main__':
    claimed_url = input('Insert a url: ')

    # create an instance of the class "JutSu" based on the url you provided
    jut = JutSu(claimed_url)

    # load data from the page you received and write it to the class parameters
    jut.load()

    # output of recorded data such as: "episode title from the web page", and "direct link to the video player"
    print(f'{jut.get_original_name()} : {jut.get_direct_link()}')
