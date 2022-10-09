/*3.WAP to represent a Zoo which consists of various types of Animals (Say Tiger, Lion, Hippo)
Identify appropriate classes and implement  their relationships. Test the implementation by writing a driver code.*/
 public class Zoo
{
    int noofanimals;
    Lion l;
    Tiger t;
    Hippo h;
       
    Zoo(int noofanimals,Lion l, Tiger t, Hippo h)
    {
        this.noofanimals=noofanimals;
        this.l=l;
        this.t=t;
        this.h=h;
    }
    int getnoofanimals()
    {
        return noofanimals;
    }
    Lion getLion()
    {
        return l;
    }
    Tiger getTiger()
    {
        return t;
    }
    Hippo getHippo()
    {
        return h;
    }
    void setnoofanimals(int noofanimals)
    {
        this.noofanimals= noofanimals;
    }
    void setLion(Lion l)
    {
        this.l=l;
    }
    void setTiger(Tiger t)
    {
        this.t=t;
    }
    void setHippo(Hippo h)
    {
        this.h=h;
    }

}