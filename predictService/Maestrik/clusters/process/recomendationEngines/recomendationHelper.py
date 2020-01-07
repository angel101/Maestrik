import pickle as pk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel

class RecomendationHelper(object):
  def __init__(self):
    self.products=pk.load(open('clusters/process/recomendationEngines/products.pk','rb'))
    self.userClusterStockTable = pk.load(open('clusters/process/recomendationEngines/userClusterStockTable.pk','rb'))
    self.products = self.products.drop_duplicates()

  def getUpsellingRecomendation(self,userData):
    try:
      testCluster = userData['cluster']
      subCluster = userData['subCluster'] if 'subCluster' in userData else None
      itemTest = userData['itemId'] if 'itemId' in userData else None
      n= userData['n']
      
      tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
      tfidf = tf.fit_transform(self.products)

      invoices = self.userClusterStockTable[self.userClusterStockTable['cluster']==testCluster]
      if testCluster ==0 and subCluster != None:
        invoices = invoices[invoices['clusterSub']==subCluster]
      if itemTest:
        invoices = invoices[invoices['StockCode']==itemTest]
      invoices = invoices['InvoiceNo']

      recomendedItems = self.userClusterStockTable[self.userClusterStockTable['InvoiceNo'].isin(invoices)].groupby(['StockCode'])['Quantity'].sum().sort_values(ascending=False)
      if itemTest:
        recomendedItems = recomendedItems.drop(itemTest)
        itemsTfidf = tfidf.transform(recomendedItems['Description'])
        selectedItemTfidf = tfidf.transform(products[itemTest]['Description'])
        
      result = self.products[self.products['StockCode'].isin(recomendedItems.head().index)][:n]
      tmpList=[]
      print(result)
      for item in result.iterrows():

        tmpList.append({"stockCode": item[1]['StockCode'], "description":item[1]['Description']})
      return {"itemList":tmpList}
    except Exception as e:
      print(e)
      return {"itemList":[]}
