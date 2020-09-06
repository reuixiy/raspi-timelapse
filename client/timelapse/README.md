## usage

```sh
# Install dependency
sudo apt install python3-pip
sudo pip3 install bottle

# Add service
sudo ln -s /home/pi/timelapse/systemd/timelapse-image.service /etc/systemd/system/
sudo ln -s /home/pi/timelapse/systemd/timelapse-server.service /etc/systemd/system/
sudo systemctl daemon-reload

# Start or stop
sudo systemctl start/stop timelapse-image.service
sudo systemctl start/stop timelapse-server.service

# Enable or disable timelapse at system boot
sudo systemctl enable/disable timelapse-image.service
sudo systemctl enable/disable timelapse-server.service
```

Full documentation on <https://github.com/reuixiy/raspi-timelapse>.
