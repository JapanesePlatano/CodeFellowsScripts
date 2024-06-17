# Script Name:                  Lua script
# Author:                       Gilbert Collado
# Date of latest revision:      06/13/2024
# Purpose:                      Lua script for nmap

description = [[
Retrieves HTTP headers from the target web server.
]]

---
-- @usage
-- nmap --script=http-headers <target>
--
-- @output
-- PORT   STATE SERVICE
-- 80/tcp open  http
-- |_http-headers: Server: Apache/2.4.41 (Ubuntu)
-- | Date: Wed, 17 Jun 2024 12:34:56 GMT
-- | Content-Type: text/html; charset=UTF-8
-- | ...

author = "Gilbert Collado"

categories = {"discovery", "safe"}

require "http"
require "shortport"

portrule = shortport.http

action = function(host, port)
  local path = "/"
  local response = http.get(host, port, path)
  if response == nil then
    return "Failed to retrieve HTTP headers"
  end

  return response["rawheader"]
end
