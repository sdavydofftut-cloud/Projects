from typing import Any, Dict, Optional
from data.constants import BASE_URL
import requests
import allure

class BaseClient:
    def __init__(self, base_url=BASE_URL, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    @allure.step("HTTP {method} {path}")
    def request(
        self,
        method: str,
        path: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        json: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        ) -> requests.Response:
        url = f"{self.base_url}{path}"
        response = self.session.request(
            method=method,
            url=url,
            headers=headers,
            json=json,
            params=params,
            timeout=self.timeout,)
        try:
            allure.attach(response.text, name="Response Body", attachment_type=allure.attachment_type.TEXT)
        except Exception:
            pass
        return response
