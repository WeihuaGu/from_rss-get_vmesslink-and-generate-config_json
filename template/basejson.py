#!/usr/bin/python
# -*- coding: UTF-8 -*- 

#生成基本json模板
basejsondic={
	"log": {
	},
	"inbounds": [
		{
			"port": 10107,
			"listen": "0.0.0.0",
			"tag": "http-inbound",
			"protocol": "http",
			"settings": {
				"auth": "noauth",
				"udp": False,
				"ip": "0.0.0.0"
			},
			"sniffing": {
				"enabled": True,
				"destOverride": ["http", "tls"]
			}

		},
                {
                        "port": 10103,
                        "listen": "0.0.0.0",
                        "protocol": "dokodemo-door",
                        "settings": {
                            "userLevel": 0,
                            "network": "tcp,udp",
                            "timeout": 30,
                            "followRedirect": True
                        },
                        "sniffing": {
                            "enabled": True,
                            "destOverride": [
                                "http",
                                "tls"
                            ]
                        }
                }

	],
	"outbounds": [

	],
	"routing": {
		"domainStrategy": "IPOnDemand",
		"rules": [{
				"type": "field",
				"outboundTag": "direct",
				"ip": [
					"geoip:private",
                                        "geoip:cn"
				]
			},
                        {
                                "type": "field",
                                "outboundTag": "direct",
                                "domain": ["geosite:cn"]
                        },
			{
				"type": "field",
				"balancerTag": "proxylist",
				"domain": ["geosite:geolocation-!cn"]
			}
		],
		"balancers": [{
				"selector": [
				],
				"tag": "proxylist"

			}


		]
	}
}




