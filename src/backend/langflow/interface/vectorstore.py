from langflow.interface.custom_lists import vectorstores_type_to_cls_dict
from langflow.settings import settings
from langflow.interface.base import LangChainTypeCreator
from langflow.utils.util import build_template_from_class
from typing import Dict, List


class VectorstoreCreator(LangChainTypeCreator):
    type_name: str = "vectorstore"

    @property
    def type_to_loader_dict(self) -> Dict:
        return vectorstores_type_to_cls_dict

    def get_signature(self, name: str) -> Dict | None:
        """Get the signature of an embedding."""
        try:
            return build_template_from_class(name, vectorstores_type_to_cls_dict)
        except ValueError as exc:
            raise ValueError(f"Vector Store {name} not found") from exc

    def to_list(self) -> List[str]:
        return [
            vectorstore
            for vectorstore in self.type_to_loader_dict.keys()
            if vectorstore in settings.vectorstores or settings.dev
        ]
