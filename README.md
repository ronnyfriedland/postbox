# Beispiel Setup

[Beispiel-Konfiguration](config.ini)

## Rf 433 MHz Sender

- RF 433 Mhz Sender-Modul Kit
- Spannung: 9V DC

- Funktioniert direkt wenn Kontakt an einem Data-Pin besteht

## Rf 433 MHz Receiver

- Superheterodyne 433 Mhz Empfänger
- Spannung: 3V DC

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
  - benötigt SSL Zertifikat unter `mail/server.pem`
- Credentials: xxx
- Sender: xxx
- Empfänger: xxx

## Vault

- KV - Backend (V2) unter "postbox" gemountet
- Ablage der Zugangsdaten
  - mailserver_host  
  - mailserver_port  
  - mailserver_username  
  - mailserver_password  
  - mailserver_sender  
  - mailserver_recipient  

