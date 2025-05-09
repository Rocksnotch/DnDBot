import gspread
from reads import getSheetURL, getSheetKey

def writeCellValue(sheetURL: str, idx: int, cell: str, value: str, client: gspread.Client) -> None:
    """Writes a value to a cell in a Google Sheet.

    Args:
        sheetURL (str): The URL of the Google Sheet
        idx (int): The index of the sheet to write the value to (0-indexed)
        cell (str): The cell to write the value to (e.g. "A1")
        value (str): The value to write to the cell
        client (gspread.Client): An instance of the class produced by `http_client` (gspread.Client)

    Returns:
        None
    """
    getSheetURL(sheetURL, client).get_worksheet(idx).update_acell(cell, value)