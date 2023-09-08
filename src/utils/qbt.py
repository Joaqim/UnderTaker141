import qbittorrentapi
import os
import re
import time

class JCQbt:
    """
    A class to interact with qBittorrent, specifically for JC141 related downloads.
    """
    def __init__(self, host, port, username, password, save_path):
        
        os.system("qbittorrent &")
        
        # connect to the client
        self.qbt_client = qbittorrentapi.Client(
            host=host,
            port=port,
            username=username,
            password=password,
        )
            
        self.save_path = save_path
            
    # get all torrents with the tag "jc141"
    def get_torrents(self):
        return self.qbt_client.torrents_info(tag="jc141")
    
    # pause torrent
    def pause(self, url):
        return self.qbt_client.torrents_pause(torrent_hashes=self.get_hash(url))
    
    # resume torrent
    def resume(self, url):
        return self.qbt_client.torrents_resume(torrent_hashes=self.get_hash(url))
    
    # delete torrent
    def delete(self, url, delete_files=False):
        return self.qbt_client.torrents_delete(torrent_hashes=self.get_hash(url), delete_files=delete_files)

    # download torrent, add tag "jc141" to easily identify
    def download(self, url):
        return self.qbt_client.torrents_add(urls=url, tags="jc141", save_path=self.save_path)
    
    # get torrent hash from magnet link
    def get_hash(self, url):
        return re.findall(r"magnet:\?xt=urn:btih:([a-zA-Z0-9]+)", url)[0]
    
    # get torrent with hash
    def get_torrent(self, url):
        return self.qbt_client.torrents_info(torrent_hashes=self.get_hash(url))[0]
