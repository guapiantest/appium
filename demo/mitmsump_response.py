from mitmproxy import http


class ABC:
  def request(self, flow: http.HTTPFlow) -> None:
        if "quote.json" in flow.request.pretty_url:
            with open('/Users/shiyoujuan/Desktop/quote.json', 'r', encoding='utf-8') as f:
                flow.response = http.HTTPResponse.make(
                    200,  # (optional) status code
                    f.read(),  # (optional) content
                    {"Content-Type": "application/json"}  # (optional) headers
                )
addons = [
    ABC()
]
