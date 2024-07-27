import os
from pathlib import Path
from typing import List

from pypdf import PdfWriter

class MergePDF:
    """
    This class merges pdf files in a repository
    """
    # Standard Stuffs
    gitignore_stuff = [
    ]

    def __init__(self, directory, style="colorful"):
        self.directory = Path(str(directory))
        self.name_repository = str(directory).strip(os.sep).split(os.sep)[-1]
        self.ignored_files = MergePDF.gitignore_stuff + self.ignore_files()
        self.files_to_merge = self.select_files(self.directory)
    
    def ignore_files(self) -> List[str]:
        """
        Scrap the gitignore file if it exists and prepare all the stuffs that must be ignored.
        :return: List of strings, that depicts the files/folders scrapped from .gitignore file.
        """

        gitignore_content = []
        if self.directory.joinpath(".gitignore").exists():
            with self.directory.joinpath(".gitignore").open() as fp:
                content = fp.readlines()
                for i in content:
                    line = i.strip()
                    if len(line) > 0 and "#" not in line:
                        gitignore_content.append(line.strip("*"))
        else:
            print(
                "Since the .gitignore file doesn't exists, all the files will be considered"
            )
        return gitignore_content

    def add_ignore_files(self, new_ignore_stuff: List[str]) -> None:
        self.ignored_files += new_ignore_stuff

    def select_files(self, directory: Path, files_selected=[]) -> List[Path]:
        """
        Discover which pdf files are allowed, then return a list with them.
        :param directory: Path
        :param files_selected: List
        :return: List of paths of selected/filtered pdf files
        """
        for i in sorted(directory.iterdir()):
            if not self.must_ignore(i) and i.is_dir():
                self.select_files(i)
            elif not self.must_ignore(i) and i.is_file():
                if i.suffix == ".pdf":
                    #print(f'Valid file -> {i}')
                    files_selected.append(i)
        return files_selected

    def must_ignore(self, filename: Path) -> bool:
        """
        Validates if a file must be ignored or not from certain logic.
        :param filename: Path
        :return: True or False
        """
        if filename.is_dir() and f"{filename.name}/" in self.ignored_files:
            return True
        elif (
                filename.is_file()
                and filename.suffix in self.ignored_files
                or filename.name in self.ignored_files
        ):
            return True

    def merge_pdf(self):
        merger = PdfWriter()
        try:
            for file in self.files_to_merge:
                merger.append(file)    
            merger.write(f"{str(self.directory)}/{self.name_repository}.pdf")
            merger.close()
            print(
                        f"File {str(self.directory)}{os.sep}{self.name_repository}.pdf merged with success!"
                    )
        except OSError:
            print("Merge failed!")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog="Merge PDF",
        description="This program merges all PDF files in a repository",
    )
    parser.add_argument("dir", type=Path, help="Path of the repository.")
    parser.add_argument(
        "--ignore",
        type=str,
        nargs='?',
        help="Add files and/or folders for ignoring.",
    )
    # Creating a Namespace object
    args = parser.parse_args()
    try:
        if Path(args.dir).exists():
            repo = MergePDF(args.dir)
            repo.merge_pdf()
        else:
            raise FileNotFoundError
    except FileNotFoundError:
        print("Invalid Folder !")
