#!/usr/bin/perl

use List::Util qw[min max];

$GOLD=$ARGV[0];
$HYP=$ARGV[1];

if(!defined($GOLD) || !defined($HYP)){die("use: <goldstandart> <hypothesis>\n");}

print STDERR "Load goldstandart\n";
open(GOLD,"$GOLD") || die("Can't open $GOLD\n");
while(<GOLD>)
{
	if(s/(\S+)\s+(\S+)//)
	{
		$ref{$1}{$2}++;
		$listeReq{$1}++;
	}
	else
	{
		print STDERR "Input format error\n";
	}
}
close(GOLD);

print STDERR "Load hypothesis\n";
open(HYP,"$HYP") || die("Can't open $HYP\n");
while(<HYP>)
{
	if(s/(\S+)\s+(\S+)\s+(\S+)//)
	{
		$hyp{$1}{$2}=$3;
		$listeReq{$1}++;
	}
	else
	{
		print STDERR "Input format error\n";
	}
}
close(HYP);

print STDERR "Compute error statistics\n";
print STDOUT "__________________________________________________________________________________________________\n";
print STDOUT "| Query  | Hypothesis | GoldSantard | Correct | Precision |   Recall  |    F1    |  P\@1  |  P\@5  |\n";
print STDOUT "|--------|------------|-------------|---------|-----------|-----------|----------|-------|-------|\n";
$nbReq=0;
foreach $req (sort{$a<=>$b} keys %listeReq)
{
	#print STDERR "\n$req:\n";
	$pa5=0;
	$pa1=0;
	my $rank=1;
	my $trouve=0;
	foreach $doc (sort{$hyp{$req}{$b}<=>$hyp{$req}{$a}} keys %{$hyp{$req}})
	{
		#print STDERR "$doc: $hyp{$req}{$doc}\n";
		if(exists($ref{$req}{$doc}))
		{
			$trouve++;
			if($rank<=1) {$pa1=1;}
			if($rank<=5) {$pa5++;}
		}
		$rank++;
	}
	$nbhyp=scalar(keys %{$hyp{$req}});
	$nbref=scalar(keys %{$ref{$req}});
	if($nbhyp>0){	$P=$trouve/$nbhyp*100.0;} else {$P=0;}
	if($nbref>0){$R=$trouve/$nbref*100.0;}else{$R=100;}
	if($P+$R>0) {$F=2*($P*$R)/($P+$R);} else {$F=0;}
	$pa1*=100;
	if($nbref>0) {$pa5*=max(20,100.0/$nbref);} elsif($nbhyp==0) {$pa5=100;} else {$pa=0;}
	printf( STDOUT "|  %3d   |   %5d    |   %5d     |   %5d | %6.1f%   | %6.1f%   |  %6.1f% |  %3.0f% |  %3.0f% |\n",$req,$nbhyp,$nbref,$trouve, $P, $R , $F,$pa1,$pa5);
	print STDOUT "|--------|------------|-------------|---------|-----------|-----------|----------|-------|-------|\n";
	
	$Ghyp+=$nbhyp;
	$Gref+=$nbref;
	$Gtrouve+=$trouve;
	$Gpa1+=$pa1;
	$Gpa5+=$pa5;
	$nbReq++;
}
if($Ghyp>0){	$P=$Gtrouve/$Ghyp*100.0;} else {$P=0;}
if($Gref>0){$R=$Gtrouve/$Gref*100.0;}else{$R=0;}
if($P+$R>0) {$F=2*($P*$R)/($P+$R);} else {$F=0;}
$Gpa1/=$nbReq;
$Gpa5/=$nbReq;
printf( STDOUT "| Overall|   %5d    |   %5d     |   %5d | %6.1f%   | %6.1f%   |  %6.1f% |  %3.0f% |  %3.0f% |\n",$Ghyp,$Gref,$Gtrouve, $P, $R , $F,$Gpa1,$Gpa5);
print STDOUT "|--------|------------|-------------|---------|-----------|-----------|----------|-------|-------|\n";
