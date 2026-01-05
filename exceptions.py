class APIError(Exception):
    def __init__(self, detail: str, status_code: int = 500):
        self.status_code = status_code
        self.detail = detail
        super().__init__(self.detail)