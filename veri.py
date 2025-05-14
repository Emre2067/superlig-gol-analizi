import matplotlib.pyplot as plt
# Takımlar ve attıkları go sayıları 
takimlar = ['Fenerbahçe','Galatasaray','Kasımpaşa','Başakşehir','Göztepe','Beşiktaş','Trabzonspor','Samsunspor','Eyüpspor','Sivasspor']
goller = [84, 84, 57, 55, 54, 53, 53, 50, 49, 44]

renkler =['blue','red','green','orange','gold','black','darkblue','darkred','yellow','green']

# Grafik çizimi 
plt.figure(figsize=(12, 7))
bars = plt.bar(takimlar , goller, color=renkler)

#Başlık ve Etiketler 
plt.title('2024-2025 Süper Lig: En Çok Gol Atan Takımlar', fontsize=14)
plt.xlabel('Takımlar', fontsize=12)
plt.ylabel('Gol Sayısı',fontsize=12)

for bar in bars:
    y = bar.get_height()
    plt.text(bar.get_x() +
bar.get_width() / 2, y + 1 , str(y), ha='center',fontsize=10)
    
plt.ylim(0 , max(goller) +10 ) #Y Eksenini Genişlet
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()    