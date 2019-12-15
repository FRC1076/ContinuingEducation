class RASReceiver:
    """
    RASReceiver listens for an announcement from the detector.
    It is created using the IP address and the port number of the detector
    and it starts up a thread that can listen for incoming announcements.
    When it has received an announcement from the detector, the hasReceivedAnnouncement()
    method will return True.   The hasReceivedAnnouncement() condition is automatically
    cleared when the function is called.
    Here's example:
    
    import RASReceiver from RASReceiver
    
    # in robotInit
    self.rasReceiver = RASReceiver('10.10.76.27', 2345)
    
    # in teleopInit
    self.rasReceiver.startListening()
    
    # in teleopPeriodic
    if self.rasReceiver.hasReceivedAnnouncement():
        self.doTheThingToDoWhenDetectorDetects()
    """
    
    def __init__(self, detector_ip, listen_port):
        self.dip = detector_ip
        self.port = listen_port
  
