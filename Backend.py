import math

class Stats:
    
    def make_group(self):
        
        self.group = [[int(a)] for a in self.entr1.get().split("-")]
        self.diff = self.group[1][0] - self.group[0][0]
        e = 0
        
        for b in range(len(self.group)):
            a = self.group[b][0] + self.diff
            c = int(self.entr2.get().split("-")[b])
            d = (self.group[b][0] + a) / 2
            e += c
            f = c * d
            self.group[b].extend([a, c, d, f, e])
        

    def constants(self):
        self.sig_mf = 0
        self.sig_f_m_min_x_bar_sq = 0
        self.sig_f = self.group[len(self.group) - 1][5]
        
        for a in range(len(self.group)):
            self.sig_mf += self.group[a][4]
            
        self.x_bar = self.sig_mf / self.sig_f
        
        for a in self.group:
            self.sig_f_m_min_x_bar_sq += (a[3] - self.x_bar) ** 2 * a[2]
                    
        self.i = self.group[0][1] - self.group[0][0]
        
        
    def f_mode(self):
        
        self.make_group()
        self.constants()
        self.g_mod = [0,0,0]
        
        for a in range(len(self.group)):
            if self.g_mod[2] < self.group[a][2]:
                self.g_mod = self.group[a]
                self.tr1 = self.tr2 = self.g_mod[2]
                
                if a != 0:
                    self.tr1 -= self.group[a - 1][2]
                    
                if a != len(self.group) - 1:
                    self.tr2 -= self.group[a + 1][2]
                    
        self.l_mod = self.g_mod[0]
        
        self.mode = round(self.l_mod + self.tr1 / (self.tr1 + self.tr2) * self.i, 2)
        return self.mode
            
            
    def f_mean(self):
        
        self.make_group()
        self.constants()
        
        self.mean = round(self.sig_mf / self.sig_f, 2)
        return self.mean
    
    
    def f_median(self):
        
        self.make_group()
        self.constants()
        
        for a in range(len(self.group)):
                    
            if self.group[a][5] > self.sig_f / 2:
                self.g_med = self.group[a]
                self.l_med = self.g_med[0]
                self.f_med = self.g_med[2]
                self.fl_med = self.g_med[5] - self.f_med
                break
            
        self.median = round(self.l_med + (self.sig_f / 2 - self.fl_med) / self.f_med * self.i, 2)
        return self.median
    
    
    def f_q1(self):
        
        self.make_group()
        self.constants()
        
        for a in range(len(self.group)):
                        
            if self.group[a][5] > self.sig_f / 4:
                self.g_q1 = self.group[a]
                self.l_q1 = self.g_q1[0]
                self.f_q1 = self.g_q1[2]
                self.fl_q1 = self.g_q1[5] - self.f_q1
                break
            
        self.q1 = round(self.l_q1 + (self.sig_f / 4 - self.fl_q1) / self.f_q1 * self.i, 2)
        return self.q1
    
    
    def f_q3(self):
        
        self.make_group()
        self.constants()
        
        for a in range(len(self.group)):
                        
            if self.group[a][5] > 3 * self.sig_f / 4:
                
                self.g_q3 = self.group[a]
                self.l_q3 = self.g_q3[0]
                self.f_q3 = self.g_q3[2]
                self.fl_q3 = self.g_q3[5] - self.f_q3
                break
            
        self.q3 = round(self.l_q3 + (3 * self.sig_f / 4 - self.fl_q3) / self.f_q3 * self.i, 2)
        return self.q3
    
    
    def f_oms(self):
        
        self.make_group()
        self.constants()
        self.sig_f_m_min_x_bar = 0
        
        for a in self.group:
            b = round(abs(a[2] * (a[3] - self.x_bar)), 2)
            self.sig_f_m_min_x_bar += b
            a.extend([b])
        
        self.oms = round(self.sig_f_m_min_x_bar / self.sig_f, 2)
        return self.oms
    
    
    def f_variance(self):
        
        self.make_group()
        self.constants()
        
        self.sig_fm_sq = 0
        
        for a in self.group:
            self.sig_fm_sq += a[3] ** 2 * a[2]
            
        self.variance = round((self.sig_fm_sq - self.sig_mf ** 2 / self.sig_f) / (self.sig_f - 1), 2)
        return self.variance
    
    
    def f_standard_deviation(self):
        
        self.make_group()
        self.constants()
        
        self.standard_deviation = round(math.sqrt(self.sig_f_m_min_x_bar_sq / (self.sig_f - 1)) ,2)
        return self.standard_deviation
    
    
    def f_skp(self):
        
        self.make_group()
        self.constants()
        
        self.skp = round((self.f_mean() - self.f_mode()) / self.f_standard_deviation(), 2)
        return self.skp
    
