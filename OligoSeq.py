class OligoSeq():
    
    def __init__(self) -> None:
        pass
    
    def oligoSeq(self, seq: str, oligo: int) -> list:
        """_summary_
        Args:
            seq (str): _description_
            oligo (int): _description_
        Returns:
            list: _description_
        """
        seq_list = []
        seq = seq + seq[:oligo]
        for j in range(oligo):
            oseq_list = [seq[idx:idx + oligo] for idx in range(j, len(seq) + j, oligo)]
            seq_list.append(oseq_list)
        return seq_list
        
    def seqOligoFrame(self, seq: str, oligo: int) -> list:
        frame_oseq = []
        
        
        return frame_oseq