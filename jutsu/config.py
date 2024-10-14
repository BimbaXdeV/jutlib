class Config:
    def __init__(self, download_res: int, name_separator: str, register_style: str = 'default'):
        self.website_protocol_trigger = 'https:'
        self.service_trigger = 'jut.su'
        self.download_resolutions = (
            1080,
            720,
            480,
            360
        )
        self.register_styles = (
            'default',
            'upper',
            'lower'
        )

        self.download_res: int = download_res if download_res in self.download_resolutions else self.download_resolutions[-1]
        self.name_separator: str = name_separator
        self.register_style: str = register_style if register_style in self.register_styles else self.register_styles[0]
