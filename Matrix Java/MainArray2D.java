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
public class MainArray2D {
    public static void main(String[] args) {
        Array2D ob= new Array2D();
        int [][]A={
            {1,2},
            {3,5},
            {6,7}};
        int[][]B={
            {8,9},
            {10,11},
            {12,13}};

        System.out.println("Matrik A :");
        ob.setMatrikA(A);
        ob.tampil(ob.getMatrikA());
        System.out.println("------------------");
        System.out.println("Matrik B :");
        ob.setMatrikB(B);
        int pengali =2;
        ob.tampil(ob.getMatrikB());
        ob.setPenjumlahan(B, A);
        System.out.println("Penjumlahan");
        ob.tampil(ob.getPenjumlahan());
        System.out.println("Perkalian");
        ob.setperkalian(ob.getPenjumlahan(), 0.5);
        ob.tampil(ob.getPeekalian());

        ob.hapus();
        A=null;
        B=null;
        ob=null;
    }
}
