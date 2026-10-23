# Modelo de compras: minimizar coste cubriendo una demanda mínima

set PROVEEDORES; # lista de proveedores (S1, S2, S3)
param Coste {PROVEEDORES}; # coste por unidad de cada proveedor
param Demanda; # cantidad mínima total a comprar

var Compra {p in PROVEEDORES} >= 0; # unidades a comprar a cada proveedor

minimize CosteTotal: # funcion objetivo
sum {p in PROVEEDORES} Coste[p] * Compra[p];

subject to DemandaMinima: # restriccion de compra minima
sum {p in PROVEEDORES} Compra[p] >= Demanda;