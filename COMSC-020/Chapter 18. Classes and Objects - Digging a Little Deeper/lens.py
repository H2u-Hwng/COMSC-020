# Huu Hung Nguyen
# 12/02/2021
# Nguyen_HuuHung_lens.py
# The program stores Lens class

class Lens:
    ''' Lens class for representing and
        manipulating forcal length, aperture coordinates. '''
    
    def __init__(self, focal_length, aperture):
        ''' Create a new lens at the given coordinates. '''
        
        self.focal_length = focal_length if focal_length > 0 else 1.0
        self.aperture = aperture if aperture > 0 else 1.0
        
    def __str__(self):
        ''' Display the focal length and the aperture. '''
        
        display = 'focal length: {:.1f}mm, aperture: {:.1f}mm'. \
                  format(self.focal_length, self.aperture)
        
        return display
    
    def __eq__(self, other):
        ''' Return True if the given coordinates are the same
            and False otherwise. '''
        
        compare = (self.focal_length and self.aperture) == \
                  (other.focal_length and other.aperture)
        
        return compare
    
    def getFocal_length(self):
        ''' Return focal length. '''
        
        return self.focal_length
    
    def getAperture(self):
        ''' Return aperture. '''
        
        return self.aperture
    
    def calc_f_stop(self):
        ''' Calculate and return lens f stop. '''
        
        lens_f_stop = self.focal_length / self.aperture
        
        return lens_f_stop
