from jutsu.downloader import JutSu


if __name__ == '__main__':
    claimed_url = input('Insert a url: ')

    # create an instance of the class and load data from the page on the main configurations
    jut = JutSu(claimed_url)
    jut.load()

    # display loaded class parameters with default configuration
    print(f'{jut.name_to_register()} : {jut.get_direct_link()}')

    # change the default configuration by inserting changed values for the parameters
    jut.configure(
        download_res=480,  # video quality category
        name_separator='-',  # parameter that will replace all spaces in the episode name
        register_style='upper'  # choose which register the names will be in
    )

    # display the received data on the changed configuration
    jut.load()
    print(f'{jut.name_to_register()} : {jut.get_direct_link()}')

