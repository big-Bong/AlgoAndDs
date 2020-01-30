def format_duration(seconds):
    #your code here
    if(seconds == 0):
        return "now"
    
    output = ""
    q_y,r_y = divmod(seconds,31536000)
    q_d,r_d = divmod(r_y,86400)
    q_h,r_h = divmod(r_d,3600)
    q_m,r_m = divmod(r_h,60)
    
    if(q_y>1):
        if(r_y == 0):
            return str(q_y)+" years"
        if((q_d > 0 and q_h > 0) or (q_d > 0 and q_m > 0) or (q_d > 0 and r_m > 0) or (q_h > 0 and q_m > 0) or (q_h >0 and r_m > 0) or (q_m > 0 and r_m > 0)):
            output += str(q_y)+" years, "
        else:
            output += str(q_y)+" years and "
    elif(q_y>0):
        if(r_y == 0):
            return "1 year"
        if((q_d > 0 and q_h > 0) or (q_d > 0 and q_m > 0) or (q_d > 0 and r_m > 0) or (q_h > 0 and q_m > 0) or (q_h >0 and r_m > 0) or (q_m > 0 and r_m > 0)):
            output += "1 year, "
        else:
            output += "1 year and "
    
    if(q_d>1):
        if(r_d == 0):
            return output+str(q_d)+" days"
        if((q_h > 0 and q_m > 0) or (q_h > 0 and r_m > 0) or (q_m > 0 or r_m > 0)):
            output += str(q_d)+" days, "
        else:
            output += str(q_d)+" days and "
    elif(q_d>0):
        if(r_d == 0):
            return output+"1 day"
        if((q_h > 0 and q_m > 0) or (q_h > 0 and r_m > 0) or (q_m > 0 or r_m > 0)):
            output += "1 day, "
        else:
            output += "1 day and "
    
    if(q_h>1):
        if(r_h == 0):
            return output+str(q_h)+" hours"
        elif(q_m > 0 and r_m > 0):
            output += str(q_h)+" hours, "
        else:
            output += str(q_h)+" hours and "
    elif(q_h>0):
        if(r_h == 0):
            return output+"1 hour"
        elif(q_m > 0 and r_m > 0):
            output += "1 hour, "
        else:
            output += "1 hour and "
    
    if(q_m>1):
        if(r_m == 0):
            return output+str(q_m)+" minutes"
        else:
            output += str(q_m)+" minutes and "
    elif(q_m>0):
        if(r_m == 0):
            return output+"1 minute"
        elif(r_m == 1):
            return output+"1 minute and 1 second"
        else:
            return output+"1 minute and "+str(r_m)+" seconds"

    if(r_m == 1):
        return output+"1 second"
    else:
        return output+str(r_m)+" seconds"

seconds = 3279186
print(format_duration(seconds))