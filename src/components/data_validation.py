import pandas as pd
from src.entity import DataValidationConfig
from src.config import logger


class DataValidation:
    def __init__(self, config: DataValidationConfig) -> None:
        """
        Initialize Datavalidation class.

        Args:
            config (DataValidationConfig) : configuration for DataValidation
        """
        self.config = config
        self.df = pd.read_csv(self.config.input_path)

    def structural_validation(self) -> bool:
        """
        check for
        -> dtype counts
        -> dataset shape
        """
        if self.__check_dtype():
            logger.info("Dataset Structure validation complted with no errors!")
            return True
        else:
            logger.error("Error in dataset structure validation")
            return False

    def integrity_validation(self) -> bool:
        """
        check for
        -> missing values
        -> duplicate values
        """
        have_missing_values = self.df.isna().sum().any() == False
        have_duplicate = any(self.df.duplicated())
        if any((have_missing_values, have_duplicate)):
            logger.error(
                f"expected 0 missing values and 0 duplidated values, but got NaN values: {self.df.isna().sum()}, Duplicates: {self.df[self.df.duplicated()].shape[0]}"
            )
            print(self.df[self.df.duplicated()])
            return False
        return True

    def run(self) -> bool:
        structure_validation = self.structural_validation()
        integretity_validation = self.integrity_validation()
        if all((structure_validation, integretity_validation)):
            logger.info("DATA VALIDATION COMPLETED!")
            return True
        else:
            logger.error("SOME MISS BEHAVE OCCURED WHILE DATA VALIDATION")
            return False

    def __check_dtype(self) -> bool:
        object_status = (
            len(self.df.select_dtypes("object").columns) == self.config.dtypes["object"]
        )

        number_status = (
            len(self.df.select_dtypes("number").columns) == self.config.dtypes["number"]
        )
        if not object_status or not number_status:
            raise Exception(
                f"expected dtype ratio, numeric : {self.config.dtypes['number']}, object : {self.config.dtypes['object']}, got intead : numeric: {len(self.df.select_dtypes('number').columns)} object : {len(self.df.select_dtypes('object').columns)}"
            )
        return True
