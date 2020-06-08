#!/usr/bin/osascript

set bucket to the text returned of (display dialog "Bucket?" default answer "" with title "alioss-config")
if bucket is not "" then
  set endpoint to the text returned of (display dialog "Endpoint?" default answer "" with title "alioss-config")
  if endpoint is not "" then
    set accessKeyId to the text returned of (display dialog "AccessKeyId?" default answer "" with title "alioss-config")
    if accessKeyId is not "" then
      set accessKeySecret to the text returned of (display dialog "AccessKeySecret?" default answer "" with title "alioss-config")
      if accessKeySecret is not "" then
        set urlPrefix to the text returned of (display dialog "Url Prefix?" default answer "" with title "alioss-config")
        if urlPrefix is not "" then
          set ret to bucket & "\n" & endpoint & "\n" & accessKeyId & "\n" & accessKeySecret & "\n" & urlPrefix
          return ret
        end if
      end if
    end if
  end if
end if
