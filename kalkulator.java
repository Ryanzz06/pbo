import java.util.Scanner;

public class OperatorAritmatika {

    public static void main(String[] args) {
        int angka1;
        int angka2;
        int hasil;

        Scanner keyboard = new Scanner(System.in);
        
#PEMJUMLAHAN
        System.out.print("MASUKKAN BILANGAN 1 = ");
        angka1 = keyboard.nextInt();
        System.out.print("MASUKKAN BILANGAN 2 = ");
        angka2 = keyboard.nextInt();
        hasil = angka1 + angka2;
        System.out.println("Hasil = " + hasil);

#PENGURANGAN
        System.out.print("MASUKKAN BILANGAN 1 = ");
        angka1 = keyboard.nextInt();
        System.out.print("MASUKKAN BILANGAN 2 = ");
        angka2 = keyboard.nextInt();
        hasil = angka1 - angka2;
        System.out.println("Hasil = " + hasil); 

#PERKALIAN
        System.out.print("MASUKKAN BILANGAN 1 = ");
        angka1 = keyboard.nextInt();
        System.out.print("MASUKKAN BILANGAN 2 = ");
        angka2 = keyboard.nextInt();
        hasil = angka1 * angka2;
        System.out.println("Hasil = " + hasil);

#PEMBAGIAN
        System.out.print("MASUKKAN BILANGAN 1 = ");
        angka1 = keyboard.nextInt();
        System.out.print("MASUKKAN BILANGAN 2 = ");
        angka2 = keyboard.nextInt();
        hasil = angka1 / angka2;
        System.out.println("Hasil = " + hasil);

#SISA BAGI
        System.out.print("MASUKKAN BILANGAN 1 = ");
        angka1 = keyboard.nextInt();
        System.out.print("MASUKKAN BILANGAN 2 = ");
        angka2 = keyboard.nextInt();
        hasil = angka1 % angka2;
        System.out.println("Hasil = " + hasil);

    }

}