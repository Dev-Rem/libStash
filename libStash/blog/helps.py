from elasticsearch_dsl import Q


class ElasticSearchPostService:
    def __init__(self, document_class_name, query, size):
        self.query = query
        self.size = size
        self.search_instance = document_class_name.search()

    def run_query_list(self):

        q = Q("bool", must=[Q("match", post=self.query)])

        search_with_query = self.search_instance.query(q).sort("_score")[0 : self.size]

        response = search_with_query.execute()
        result = response.to_dict()["hits"]["hits"]

        return result