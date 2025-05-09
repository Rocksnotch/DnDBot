import gspread

def getSheetURL(sheetURL: str, client: gspread.Client) -> gspread.Spreadsheet:
    """Opens a spreadsheet specified by its `URL`.
    This function is a wrapper around `gspread.Client.open_by_url` and returns a `~gspread.models.Spreadsheet` instance.

    Args:
        sheetURL (String): The URL of the Google Sheet
        client (Client): An instance of the class produced by `http_client` (gspread.Client)

    Returns:
        gspread.models.Spreadsheet: a `~gspread.models.Spreadsheet` instance.
    """
    try:
        return client.open_by_url(sheetURL)
    except gspread.exceptions.SpreadsheetNotFound:
        raise ValueError(f"Spreadsheet with URL {sheetURL} not found. Please check the URL and try again.")

def getSheetKey(sheetKEY: str, client: gspread.Client) -> gspread.Spreadsheet:
    """Opens a spreadsheet specified by its `key`.
    This function is a wrapper around `gspread.Client.open_by_key` and returns a `~gspread.models.Spreadsheet` instance.

    Args:
        sheetURL (String): The key of the Google Sheet
        client (Client): An instance of the class produced by `http_client` (gspread.Client)

    Returns:
        gspread.models.Spreadsheet: a `~gspread.models.Spreadsheet` instance.
    """
    try:
        return client.open_by_key(sheetKEY)
    except gspread.exceptions.SpreadsheetNotFound:
        raise ValueError(f"Spreadsheet with key {sheetKEY} not found. Please check the key and try again.")

def getCellValue(sheetURL: str, idx: int, cell: str, client: gspread.Client) -> str:
    """Gets the value of a cell in a Google Sheet.

    Args:
        sheetURL (str): The URL of the Google Sheet
        idx (int): The index of the sheet to get the value from (0-indexed)
        cell (str): The cell to get the value from (e.g. "A1")
        client (gspread.Client): An instance of the class produced by `http_client` (gspread.Client)

    Returns:
        str: The value of the cell
    """
    return getSheetURL(sheetURL, client).get_worksheet(idx).acell(cell).value

def getCellFormula(sheetURL: str, idx: int, cell: str, client: gspread.Client) -> str:
    """Gets the formula of a cell in a Google Sheet.

    Args:
        sheetURL (str): The URL of the Google Sheet
        idx (int): The index of the sheet to get the value from (0-indexed)
        cell (str): The cell to get the value from (e.g. "A1")
        client (gspread.Client): An instance of the class produced by `http_client` (gspread.Client)

    Returns:
        str: The formula of the cell
    """
    return getSheetURL(sheetURL, client).get_worksheet(idx).acell(cell).formula_value

def getCellValues(sheetURL: str, idx: int, cellRange: str, client: gspread.Client) -> list:
    """Gets the values of a range of cells in a Google Sheet.

    Args:
        sheetURL (str): The URL of the Google Sheet
        idx (int): The index of the sheet to get the value from (0-indexed)
        cellRange (str): The range of cells to get the value from (e.g. "A1:B2")
        client (gspread.Client): An instance of the class produced by `http_client` (gspread.Client)

    Returns:
        list: The values of the cells
    """
    return getSheetURL(sheetURL, client).get_worksheet(idx).get(cellRange)

def getCellNotes(sheetURL: str, idx: int, cellRange: str, client: gspread.Client) -> list:
    """Gets the notes of a range of cells in a Google Sheet.

    Args:
        sheetURL (str): The URL of the Google Sheet
        idx (int): The index of the sheet to get the value from (0-indexed)
        cellRange (str): The range of cells to get the value from (e.g. "A1:B2")
        client (gspread.Client): An instance of the class produced by `http_client` (gspread.Client)

    Returns:
        list: The notes of the cells
    """
    return getSheetURL(sheetURL, client).get_worksheet(idx).get_notes(cellRange)