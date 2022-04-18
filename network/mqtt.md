# MQTT
- MQTT는 M2M, IOT를 위한 프로토콜로서, 최소한의 전력과 패킷량으로 통신하는 프로토콜
- MQTT는 HTTP, TCP등의 통신과 같이 클라이언트-서버 구조로 이루어지는 것이 아닌, Broker, Publisher, Subscriber 구조
- Publisher는 Topic을 발행(publish) 하고, Subscriber는 Topic에 구독(subscribe)합니다. Broker는 이들을 중계하는 역할
## MQTT 브로커 구동하기
MQTT 프로토콜을 구현하는 브로커들은 아래와 같이 여러 것들이 있습니다.
- Mosquitto
- HiveMQ
- mosca
- ActiveMQ
- RabbitMQ (Plug-in 형태로 지원)
## 관련 링크
https://medium.com/@jspark141515/mqtt%EB%9E%80-314472c246ee