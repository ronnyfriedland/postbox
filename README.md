# Beispiel Setup

[Beispiel-Konfiguration](config.ini)

## Rf 433 MHz Sender

- TB195 Encoder Transmitter
- Spannung: 5V DC

- Funktioniert direkt wenn Kontakt an einem Data-Pin besteht

## Rf 433 MHz Receiver

- Superheterodyne 433 Mhz Empfänger
- Spannung: 5V DC

- Anschluss an RaspberryPi Pin 19
- Rf Signal-Zeichenkette: 5592512 

## Mosquitto - Docker

- Host: 192.168.8.10
- Port 8883
- SSL enabled
  - benötigt SSL Zertifikat unter `mqtt/server.pem`
- Topic: test/postbox
- Credentials: xxx

## Subscriber

### InfluxDB

- Host: 192.168.8.10
- Port 8086
- Credentials: xxx
- Database: postbox

### E-Mail

- Host: 192.168.8.10
- Port 465
- SSL enabled
- Credentials: xxx
- Sender: xxx
- Empfänger: xxx

