class Tweet :
    def __init__(self,tweet) :
        self.id = str(tweet['id'])
        self.words = tweet['words']
        self.time = tweet['time']
        self.user = tweet['user']
    
    def __lt__(self,rhs) :
        if len(self.words) > len(rhs.words) :
            return True

        elif len(self.words) == len(rhs.words) :
            if self.time > rhs.time :
                return True
            return False

        return False 

    def __str__(self) :
        return(self.time + ': [' + self.user + '] ' + ' '.join(self.words) + ' (' + self.id + ')')
    
    def similarity(self,other) :
        n = 0

        for i in self.words :
            for j in other.words :
                if i == j :
                    n += 1
        return n
    
def show_tweets(tweets) :
    tweets.sort()
    for i in tweets :
        print(i)

def find_similarity(tweets) :
    l = []
    m = 1

    for i in range(len(tweets)):
        for j in range(m,len(tweets)) :
            l.append((tweets[i].similarity(tweets[j]),i+1,j+1))
        m += 1
        
    l.sort()
    return l
        
tw1=Tweet({'id':1,'user':'abc','words':['this','is','a','blockchain','made','from','scratch','in','~50','lines','of','python','code'],'time':'2021-11-18 16:38'})
tw2=Tweet({'id':2,'user':'cdg','words':['javascript', 'java', 'python', 'php', 'and', 'their', 'learning', 'curves'],'time':'2021-11-06 14:28'})
tw3=Tweet({'id':3,'user':'def123','words':['python', 'and', 'javascript'],'time':'2021-11-01 07:55'})
tw4=Tweet({'id':4,'user':'def123','words':['java','and','python'],'time':'2021-11-01 07:56'})
tweets=[tw1,tw2,tw3,tw4]

print(find_similarity(tweets))