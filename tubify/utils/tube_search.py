from youtube_search import YoutubeSearch
import json


class Tube_search(object):
    def __init__(self, search_query, max_res):
        self._query = search_query
        self._max_res = max_res
        self.info_list = []

    def get_search_query(self):
        return self._query
    
    def get_max_res(self):
        return self._max_res
    
    def get_info(self):
        query = self.get_search_query()
        max_res = self.get_max_res()
        results = YoutubeSearch(query, max_results=max_res).to_json() 

        res_dict = json.loads(results)
        for res in res_dict["videos"]:
            info = {}
            info["v_title"] = res.get("title", None)
            info["v_views"] = res.get("views", None)
            info["v_id"] = res.get("id", None)
            info["v_thumb"] = res.get("thumbnails", None)[0]
            info["v_url_suffix"] = res.get("url_suffix", None).rsplit('=')[1]

            #append dictionary to info list
            self.info_list.append(info)

        return self.info_list #retun info list contains dictionary of video details

    def __str__(self):
        try:
            for item in self.info_list:
                print(item.get("v_title", None))
        except TypeError:
            pass
