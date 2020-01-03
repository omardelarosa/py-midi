# Example from: https://github.com/samaaron/sonic-pi/blob/master/etc/doc/tutorial/12.1-Receiving-OSC.md

sc = scale :C3, :major

Z = -1

live_loop :foo do
    use_real_time
    arr = sync "/osc/trigger/prophet"
    n_arr = arr + []
    t = n_arr.pop
    n_arr.each do |n|
    nt = sc[0] + n
    puts "note: #{nt}"
        if n != Z
          synth :prophet, note: nt , cutoff: 60, sustain: t
        end
    end
end