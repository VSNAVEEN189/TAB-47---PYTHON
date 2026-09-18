'''URL PARSER
Parsing structured text with string methods only
Given a URL string, break it into parts using only string methods (no urllib):
• protocol (before ://)
• domain (after :// up to the next /)
• path (after the domain)
• query parameters as key/value pairs (after the ?)'''


url = "https://shop.tab47.com/items/list?category=books&sort=price"
protocol, rest = url.split("://", 1)
if "?" in rest:
  base_part, query_string = rest.split("?", 1)
else:
  base_part, query_string = rest, ""
if "/" in base_part:
  domain, path_part = base_part.split("/", 1)
  path = "/" + path_part
else:
  domain, path = base_part, ""
query_params = {}
if query_string:
  pairs = query_string.split("&")
  for pair in pairs:
    if "=" in pair:
      key, value = pair.split("=", 1)
      query_params[key] = value
print("Protocol:", protocol)
print("Domain:", domain)
print("Path:", path)
print("Query:")
for k, v in query_params.items():
  print(f"  {k} = {v}")