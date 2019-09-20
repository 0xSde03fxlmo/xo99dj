PORT = 19543

# name -> secret (32 hex chars)
USERS = {
    "tg":  "00000000000000000000000000000000",
    "tg2": "6d6af7f1553dd34256aab711100eef14"
}

# Makes the proxy harder to detect
# Can be incompatible with very old clients
SECURE_ONLY = True

# Makes the proxy even more hard to detect
# Compatible only with the recent clients
# TLS_ONLY = True

# The domain for TLS, bad clients are proxied there
# Use random existing domain, proxy checks it on start
# TLS_DOMAIN = "www.google.com"

# Tag for advertising, obtainable from @MTProxybot
AD_TAG = "3f4d0ac097c77555759fcabd72b8e679"
