#!/usr/bin/python
# -*- coding: UTF-8 -*- 

#生成基本json模板
basejsondic={
	"log": {
	},
	"inbounds": [
		{
			"port": 1010,
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
					"geoip:private"
				]
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




