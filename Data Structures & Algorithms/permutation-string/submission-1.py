from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False
            
        # 統計 s1 的字元頻率與 s2 第一個等長窗口的字元頻率
        s1_count = Counter(s1)
        window_count = Counter(s2[:len1])
        
        # 如果剛好一開始的第一個窗口就吻合
        if s1_count == window_count:
            return True
            
        # 開始滑動窗口
        for r in range(len1, len2):
            # 1. 右邊進來一個新字元
            right_char = s2[r]
            window_count[right_char] += 1
            
            # 2. 左邊滑出去一個舊字元（窗口左界是 r - len1）
            left_char = s2[r - len1]
            window_count[left_char] -= 1
            
            # 如果左邊字元的數量歸零了，從字典中刪除它（保持 Counter 乾淨，方便比對）
            if window_count[left_char] == 0:
                del window_count[left_char]
                
            # 3. 比對當前窗口與 s1 的頻率是否完全相同
            if s1_count == window_count:
                return True
                
        return False