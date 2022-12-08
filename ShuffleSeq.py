import random

class ShuffleSeq():
    def __init__(self) -> None:
        pass
    
    def shuffleSeq(self, seq: str, oligo: int) -> list:
        """_summary_
        Shuffle seq by oligonucleotides.
        Up to 6 oligos
        Args:
            seq (str): _description_
            input sequence.
            oligo (int): _description_
            length of oligonucleotides.
        Returns:
            shuffle_seq_list (list): _description_
            shuffled sequence.
        """
        oseq = seq + seq[:oligo]
        yield seq

        for j in range(oligo):
            oseq_list = [oseq[idx:idx + oligo] for idx in range(j, len(seq)+j, oligo)]
            shuffle_oseq_list = random.sample(oseq_list, len(oseq_list))
            yield ''.join(shuffle_oseq_list)

def test():
    seq = "aaacagatcacccgctgagcgggttatctgtt"
    for item in ShuffleSeq().shuffleSeq(seq, 4):
        print (item)
        
    from OligoSeq import OligoSeq
    list_seq = OligoSeq().oligoSeq(seq, 3)
    [print(item) for item in list_seq]

if __name__ == "__main__":
    test()
    