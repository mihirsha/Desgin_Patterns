from DriveStratergy.driveStratergies import DriveStratergy

class vehicle():

    def __init__(self, drive_Strat: DriveStratergy):
        self.drive_Strat = drive_Strat
    
    def drive(self):
        self.drive_Strat.drive(self)
