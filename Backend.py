import math
import pandas


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
        try:
            self.skp = round((self.f_mean() - self.f_mode()) / self.f_standard_deviation(), 2)
            return self.skp
        except:
            self.skp = round(3 * (self.f_mean() - self.f_median()) / self.f_standard_deviation(), 2)
            return self.skp
    

    def f_ex(self):
        row1 = [float(a) for a in self.entr1.get().split('-')]
        row2 = [float(a) for a in self.entr2.get().split('-')]
        ans = 0
        for a in range(len(row1)):
            ans += row1[a] * row2[a]
        return round(ans, 2)
    
    
    def f_ex2(self):
        row1 = [float(a) for a in self.entr1.get().split('-')]
        row2 = [float(a) for a in self.entr2.get().split('-')]
        ans = 0
        for a in range(len(row1)):
            ans += row1[a] ** 2 * row2[a]
        return round(ans, 2)
    
    
    def f_varx(self):
        return round(self.f_ex2() - self.f_ex() ** 2, 2)
    
    
    def f_smean(self):
        return round(pandas.DataFrame([ float(a) for a in self.entr1.get().split('-')]).mean(), 2)
    
    
    def f_smode(self):
        return round(pandas.DataFrame([ float(a) for a in self.entr1.get().split('-')]).mode(), 2)
    
    
    def f_smedian(self):
        return round(pandas.DataFrame([ float(a) for a in self.entr1.get().split('-')]).median(), 2)
    
    
    def f_sq1(self):
        group = [float(a) for a in self.entr1.get().split('-')]
        n = (len(group) + 1) // 4 - 1
        return round(group[n] + 3 / 4 * (group[n +1] - group[n]), 2)
        
        
    def f_sq3(self):
        group = [float(a) for a in self.entr1.get().split('-')]
        n = 3 * (len(group) + 1) // 4 - 1
        return round(group[n] + 1 / 4 * (group[n +1] - group[n]), 2)
    
    
    def f_sstandard_deviation(self):
        group = pandas.DataFrame([float(a) for a in self.entr1.get().split('-')])
        x_bar = group.mean()
        return round(math.sqrt(sum([(float(a) - x_bar) ** 2 for a in self.entr1.get().split('-')]) / (len(group) - 1)), 2)
    
    
    def f_svariance(self):
        group_length = len([float(a) for a in self.entr1.get().split('-')])
        b = sum([float(a) for a in self.entr1.get().split('-')]) ** 2
        a = sum([float(a) ** 2 for a in self.entr1.get().split('-')])
        return round(math.sqrt((a - b ** 2 / group_length) / (group_length - 1)), 2)
    
    
    def f_soms(self):
        group = pandas.DataFrame([float(a) for a in self.entr1.get().split('-')])
        x_bar = group.mean()
        return round(sum([abs(float(a) - x_bar) for a in self.entr1.get().split('-')]) / len(group), 2)
    
    
    def f_sskp(self):
        try:
            return round((self.f_smean() - self.f_smode()) / self.f_sstandard_deviation(), 2)
        except:
            return round(3 * (self.f_smean() - self.f_smedian()) / self.f_sstandard_deviation(), 2)
        
        
    def f_alpha4(self):
        group = pandas.DataFrame([float(a) for a in self.entr1.get().split('-')])
        x_bar = group.mean() 
        m4 = sum([(float(a) - x_bar) ** 4 for a in self.entr1.get().split('-')])
        return round(m4 / len(group) / (self.f_sstandard_deviation() ** 4), 2)

        
