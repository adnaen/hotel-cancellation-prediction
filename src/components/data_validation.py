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
        self.df = load_csv(
            path=self.config.input_path, parse_dates=["reservation_status_date"]
        )

    def structural_validation(self) -> bool:
        """
        check for
        -> column types
        -> no.of columns
        """
        is_dtype_valid = check_dtypes(
            df=self.df, base_type_counts=self.config.dtype_counts
        )
        is_no_of_columns_equal = (
            True if self.config.no_of_columns == len(self.df.columns) else False
        )
        if all((is_dtype_valid, is_no_of_columns_equal)):
            logger.info("Structural validation complted with no errors!")
            return True
        else:
            logger.error("Error in structural validation function")
            return False

    def integrity_validation(self) -> bool:
        """
        check for
        -> missing values
        -> duplicate values
        """
        have_missing_Values = is_empty_missing_values(df=self.df)
        have_duplicate = any(self.df.duplicated())
        if any((have_missing_Values, have_duplicate)):
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
