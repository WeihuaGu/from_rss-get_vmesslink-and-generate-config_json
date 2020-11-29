#!/usr/bin/python
# -*- coding: UTF-8 -*- 

#生成基本json模板
outbound={
            "protocol": "vmess",
            "settings": {
                "vnext": [
                    {
                        "address": "",
                        "port": 0,
                        "users": [
                            {
                                "alterId": 0,
                                "id": "",
                                "level": 0,
                                "security": "auto"
                            }
                        ]
                    }
                ]
            },
            "streamSettings": {
                "network": "ws",
                "wsSettings": {
                    "path": "/v2ray"
                }
            }
 }



