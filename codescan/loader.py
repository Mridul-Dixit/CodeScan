from git import Repo
from langchain_community.document_loaders.generic import GenericLoader
from langchain.document_loaders.parsers import LanguageParser
from langchain.text_splitter import Language

def load_repo(repo_url, repo_path="./repo"):
    """
    Load a Git repository from the specified path.

    :param repo_path: Path to the Git repository.
    :return: A Repo object representing the loaded repository.
    """
    try:
        repo = Repo.clone_from(repo_url, to_path=repo_path)
        return repo
    except Exception as e:
        raise RuntimeError(f"Failed to load repository at {repo_path}: {e}")

def load_documents_from_repo(repo_path):
    """
    Load documents from the specified Git repository matching the given file pattern.

    :param repo_path: Path to the Git repository.
    :return: A list of documents loaded from the repository.
    """
    try:
        loader = GenericLoader.from_filesystem(
            repo_path,
            glob= "**/*",
            suffixes=[".py"],
            parser=LanguageParser(language=Language.PYTHON, parser_threshold=500)
        )
        documents = loader.load()
        return documents
    except Exception as e:
        raise RuntimeError(f"Failed to load documents from repository: {e}")
    
