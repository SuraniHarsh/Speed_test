import speedtest

def speed_test():

    st = speedtest.Speedtest()

    print("Your Downlod Speed is", st.download()//10**6,"Mbps")

    print("Your Upload Speed is", st.upload()//10**6,"Mbps")

    print("Your Ping is",int(st.results.ping),"MS")

speed_test()
a = input("Press Enter for Exit:")