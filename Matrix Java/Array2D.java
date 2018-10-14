/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package praktikum4;

/**
 *
 * @author Human_Error
 */
public class Array2D {

    /**
     * @param args the command line arguments
     */
    private int[][] MatrikA;
    private int[][] MatrikB;
    double [][]penjumlahan,perkalian;
    int[][] data,hasil;

    public void setMatrikA(int[][] MatrikA){
        this.MatrikA=MatrikA;
        MatrikA=null;
    }
    public int[][] getMatrikA(){
        return MatrikA;
    }
    public void setMatrikB(int[][] MatrikB){
        this.MatrikB=MatrikB;
        MatrikA=null;
    }
    public int[][] getMatrikB(){
        return MatrikB;
    }
    public void setData(int[][]data){
        this.data=data;
        data=null;
    }

    public int[][] getData(){
        return data;
    }
    public void setPenjumlahan(int[][]data,int [][] a){
        int [][]bar = new int[data.length][data[0].length];
        int i,j;
        for(i = 0; i<data.length;i++){
            for(j = 0; j<data[i].length; j++){
                bar[i][j]= data[i][j]+a[i][j];
            }
        }
        hasil = bar;
    }
    public int[][] getPenjumlahan(){
        return hasil;
    }
    public void tampil(String a){
        System.out.println(a);
        a=null;
    }
    public void setperkalian(int[][]data, double kali){
        double[][]perkali=new double[data.length][data[0].length];
        int i,j;
        for(i=0;i<data.length;i++){
            for(j=0;j<data[i].length;j++){
                perkali[i][j]=data[i][j]*(kali);
            }
        }
        perkalian = perkali;
    }
    public double[][] getPeekalian(){
        return perkalian;
                
    }
    public void tampil(double [][]data){
        int i,j;
        for(i=0;i<data.length;i++){
            for(j=0;j<data[i].length;j++){
                System.out.print(data[i][j]+"   ");
            }
            System.out.println();
        }
        data=null;
    }
    public void tampil(String data[][]){
        int i,j;
        for(i=0;i<data.length;i++){
            for(j=0;j<data[i].length;j++){
                System.out.print(data[i][j]+"   ");
            }
            System.out.println();
        }
        data=null;
    }
    public void tampil(int data[][]){
        int i,j;
        for(i=0;i<data.length;i++){
            for(j=0;j<data[i].length;j++){
                System.out.print(data[i][j]+"   ");
            }
            System.out.println();
        }
        data=null;
    }
    public void hapus(){
        MatrikA=null;
        MatrikB=null;
        data=null;
        hasil=null;
    }

}

