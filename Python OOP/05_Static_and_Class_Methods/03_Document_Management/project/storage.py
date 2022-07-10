from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = list()
        self.topics = list()
        self.documents = list()

    def __get_category_by_id(self, category_id: int):
        for category in self.categories:
            if category_id == category.id:
                return category

    def __get_topic_by_id(self, topic_id: int):
        for topic in self.topics:
            if topic_id == topic.id:
                return topic

    def __get_document_by_id(self, document_id: int):
        for document in self.documents:
            if document_id == document.id:
                return document

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category_to_edit = self.__get_category_by_id(category_id)
        category_to_edit.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic_to_edit = self.__get_topic_by_id(topic_id)
        topic_to_edit.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document_to_edit = self.__get_document_by_id(document_id)
        document_to_edit.edit(new_file_name)

    def delete_category(self, category_id: int):
        category_to_delete = self.__get_category_by_id(category_id)
        self.categories.remove(category_to_delete)

    def delete_topic(self, topic_id: int):
        topic_to_delete = self.__get_topic_by_id(topic_id)
        self.topics.remove(topic_to_delete)

    def delete_document(self, document_id: int):
        document_to_delete = self.__get_document_by_id(document_id)
        self.documents.remove(document_to_delete)

    def get_document(self, document_id: int):
        return self.__get_document_by_id(document_id)

    def __repr__(self):
        linesep = "\n"
        return linesep.join(str(document) for document in self.documents)
