media<-function(x){
  y<-sum(x)/length(x)
  return(y)
}

mediana<-function(x){
  y<-sort(x)
  if(length(x)%%2==1){
    return(y[length(x)%/%2+1])
  }else{
    return(sum(y[length(x)%/%2], y[length(x)%/%2+1])/2)
  }
}

moda<-function(x){
  y<-unique(x)
  return(y[which.max(tabulate(match(x,y)))])
  
}

a<-c(3,5,2,6,5,9,5,2,8,6)
b<-c(20,9,7,2,12,7,20,15,7)
c<-c(51.6,48.7,50.3,49.5,48.9)
d<-c(15,18,20,13,10,16,14,20)

media(a)
media(b)
media(c)
media(d)

mediana(a)
mediana(b)
mediana(c)
mediana(d)

moda(a)
moda(b)
moda(c)
moda(d)
