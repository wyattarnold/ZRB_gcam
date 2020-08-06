
clear
clc

%% load data
load -ascii ../data/Jsim.txt    % performance of the historical operations over the 2439 interdependent scenarios 
                        % (- hydropower production, irrigation deficit, environmental deficit)
load -ascii ../data/idRCP.txt   % indexes associating each scenario to a RCP (2.6, 4.5, 8.5)

% RCP colors
c26 = [13 114 186]/255;
c45 = [118 172 66]/255;
c85 = [216 84 39]/255;

%% compute ECDF separated for RCP
[Fh26,Xh26] = ecdf(Jsim(idRCP(:,1)>0,1)) ; % hydropower - RCP2.6
[Fh45,Xh45] = ecdf(Jsim(idRCP(:,2)>0,1)) ; % hydropower - RCP4.5
[Fh85,Xh85] = ecdf(Jsim(idRCP(:,3)>0,1)) ; % hydropower - RCP8.5

[Fi26,Xi26] = ecdf(sqrt(Jsim(idRCP(:,1)>0,2))) ; % irrigation deficit - RCP2.6
[Fi45,Xi45] = ecdf(sqrt(Jsim(idRCP(:,2)>0,2))) ; % irrigation deficit - RCP4.5
[Fi85,Xi85] = ecdf(sqrt(Jsim(idRCP(:,3)>0,2))) ; % irrigation deficit - RCP8.5

[Fe26,Xe26] = ecdf(sqrt(Jsim(idRCP(:,1)>0,3))) ; % environmental deficit - RCP2.6
[Fe45,Xe45] = ecdf(sqrt(Jsim(idRCP(:,2)>0,3))) ; % environmental deficit - RCP4.5
[Fe85,Xe85] = ecdf(sqrt(Jsim(idRCP(:,3)>0,3))) ; % environmental deficit - RCP8.5

%% plot figure
figure; 
subplot(221); plot( -Xh26, Fh26, 'Color', c26 );
hold on; plot( -Xh45, Fh45, 'Color', c45 );
hold on; plot( -Xh85, Fh85, 'Color', c85 );
xlabel('hydropower production (TWh/y)'); ylabel('ECDF');
subplot(222); plot( Xi26, Fi26, 'Color', c26 );
hold on; plot( Xi45, Fi45, 'Color', c45 );
hold on; plot( Xi85, Fi85, 'Color', c85 );
xlabel('irrigation deficit (m^3/s)'); ylabel('ECDF');
subplot(223); plot( Xe26, Fe26, 'Color', c26 );
hold on; plot( Xe45, Fe45, 'Color', c45 );
hold on; plot( Xe85, Fe85, 'Color', c85 );
xlabel('environmental deficit (m^3/s)'); ylabel('ECDF');
