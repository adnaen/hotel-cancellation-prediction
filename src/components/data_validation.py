from src.entity import DataValidationConfig
from src.utils import load_csv
from src.config import logger


class DataValidation:
    def __init__(self, config: DataValidationConfig) -> None:
        """
        Initialize Datavalidation class.

        Args:
            config (DataValidationConfig) : configuration for DataValidation
        """
        self.config = config
        self.df = load_csv(path=self.config.input_path)

    def structural_validation(self) -> bool:
        """
        check for
        -> dtype counts
        -> dataset shape
        """
        dtype_number_count = (
            len(self.df.select_dtypes("number")) == self.config.dtypes["number"]
        )
        dtype_object_count = (
            len(self.df.select_dtypes("object")) == self.config.dtypes["object"]
        )
        is_shape = self.df.shape == (
            self.config.shape["columns"],
            self.config.shape["rows"],
        )

        if all((dtype_object_count, dtype_number_count, is_shape)):
            logger.info("Dataset Structure validation complted with no errors!")
            return True
        else:
            logger.error(
                "Error in dataset structure validation, something not work as excepted"
            )
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
                "have duplicate or missing values, cannot proceed with integrity_validation"
            )
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
