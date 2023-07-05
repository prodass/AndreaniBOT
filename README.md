# AndreaniBOT
Bot para trackear un envío de andreani.

La idea del bot es que cada 30min consume la api en busca de un nuevo estado y lo informa mediante un bot de telegram. Nose si es la mejor implementacion pero es lo primero que se me ocurrio. :D 

Para ejecutarlo primero deben crear su propio bot, obtener el token y el chat_id. Luego deben poner el numero de seguimiento donde esta el mio en la URL de la API y listo, cada 30min se va a fijar si hay cambios :)

(Tienen el Dockerfile por si lo quieren implementar en su servidor como yo y los datos de token y chat_id para tener una idea de como es)
