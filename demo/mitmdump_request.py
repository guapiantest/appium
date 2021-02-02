"""Send a reply from the proxy without sending any data to the remote server."""

from mitmproxy import http

class MitmDemo:
    def request(self, flow: http.HTTPFlow) -> None:
        if "baidu" in flow.request.pretty_url:
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                b"Hello BaiDu",  # (optional) content
                {"Content-Type": "text/html"}  # (optional) headers
            )
addons = [
    MitmDemo()
]
