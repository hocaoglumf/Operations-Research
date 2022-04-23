:-dynamic rpath/2.      % ters liste
 
%edge(a,b,7).
%edge(a,c,9).
%edge(b,c,10).
%edge(b,d,15).
%edge(c,d,11).
%edge(d,e,6).
%edge(a,f,14).
%edge(c,f,2).
%edge(e,f,9).
 



path(From,To,Dist) :- edge(To,From,Dist).
path(From,To,Dist) :- edge(From,To,Dist).
 
shorterPath([H|Path], Dist) :-		       % path < stored path? değiştir
	rpath([H|T], D), !, Dist < D,          % Hedef düğümü eşleştir [H|_]
	retract(rpath([H|_],_)),
	assert(rpath([H|Path], Dist)).
shorterPath(Path, Dist) :-		       % aksi durumda yeni bir path bul 
	assert(rpath(Path,Dist)).
 
traverse(From, Path, Dist) :-		    %ulaşılabilir tüm düğümleri gez
	path(From, T, D),		    % her bir komşu için 
	not(memberchk(T, Path)),	    %	ziyaret edilmemişse
	shorterPath([T,From|Path], Dist+D), %	En kısa mesafe ve yolu güncelle
	traverse(T,[From|Path],Dist+D).	    %	sonra komşuyu gez
 
traverse(From) :-
	retractall(rpath(_,_)),           % çözümü sil
	traverse(From,[],0).              % başlangıçtan gez
traverse(_).
 
go(From, To) :-
	traverse(From),                   % tüm mesafeleri bul
	rpath([To|RPath], Dist)->         % Eğer hedefe ulaşıldıysa
	  reverse([To|RPath], Path),      % yolu ve mesafeyi yaz
	  Distance is round(Dist),
	  writef('En kisa yol %w mesafe %w = %w\n',
	       [Path, Dist, Distance]);
	writef('Rota bulunamadı  %w - %w\n', [From, To]).
	
